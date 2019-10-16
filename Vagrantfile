PUBLIC = 2
PRIVATE = 3
BOX = "hashicorp/bionic64"
Vagrant.configure("2") do |config|
    config.vm.provider "virtualbox" do |v|
        v.memory = 512
    end
    (1..PUBLIC).each do |machine_id|
        config.vm.define "public#{machine_id}" do |machine|
            machine.vm.box = BOX
            machine.vm.hostname = "public#{machine_id}"
            machine.vm.network "private_network", ip: "192.168.77.#{1+machine_id}"
        end
    end
    (1..PRIVATE).each do |machine_id|
        config.vm.define "private#{machine_id}" do |machine|
            machine.vm.box = BOX
            machine.vm.hostname = "private#{machine_id}"
            machine.vm.network "private_network", ip: "192.168.77.#{1+PUBLIC+1+machine_id}"
        end
    end
    # control
    config.vm.define "control1"  do |machine|
        machine.vm.box = BOX
        machine.vm.hostname = "control1"
        machine.vm.network "private_network", ip: "192.168.77.#{1+PUBLIC+1+PRIVATE+1}"
        machine.vm.provision :ansible do |ansible|
            ansible.groups = {
                "public" =>   (1..PUBLIC).to_a.map { |mid| "public#{mid}" },
                "private" =>  (1..PRIVATE).to_a.map { |mid| "private#{mid}" } + ["control1"]
            }
            ansible.limit = "all"
            ansible.become = true
            ansible.playbook = "playbook_test.yml"
        end
    end
    
end