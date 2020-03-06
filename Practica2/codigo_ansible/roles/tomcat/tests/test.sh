# Role dependency
ansible-galaxy install -r requirements.yml -f -p roles

# Run the role/playbook with ansible-playbook
ansible-playbook test.yml -i inventory

# Run the role/playbook again, checking to make sure it is idempotent
ansible-playbook test.yml -i inventory | tee ansible_test.output

result=0

declare -a arr=("centos7")
for i in "${arr[@]}"
do
	if grep -q "${i}\s*:\s*ok=10\s*changed=0\s*unreachable=0\s*failed=0" ansible_test.output ; then
		echo "[$i] Idempotence test: pass"
	else
		echo "[$i] Idempotence test: fail"
		result=100
	fi
done

# Stop docker images
ansible-playbook test.yml -i inventory -e "docker_dynamic_inventory_provisioner_stop=True" -l "localhost"

exit $result