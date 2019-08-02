import pexpect


user_name = 'admin'
ip_address = ' '
ssh_cmd = "ssh " + user_name + "@" + ip_address
prompt_list = '#'
password = ' '
child = pexpect.spawn(ssh_cmd)
if child is not None:
    i = child.expect(['password:', '(yes/no)', pexpect.TIMEOUT, pexpect.EOF], timeout=30)
    # If password prompt
    if i == 0:
        print (child.before)
        child.sendline(password)
        child.expect(prompt_list)
        # print child.before
        #child.expect(pexpect.EOF)
        power_cycle_cmd = 'power outlets 1 cycle'
        child.sendline(power_cycle_cmd)
        # i = child.expect(['outlet', pexpect.TIMEOUT, pexpect.EOF], timeout=30)
        child.expect('y/n')
        child.sendline('y')
        child.expect(prompt_list)
        print (child.before)
    elif i == 1:
        print (child.before)
        child.sendline('yes')
        i = child.expect(['[P/p]assword:', '(yes/no)', pexpect.TIMEOUT, pexpect.EOF], timeout=30)
        print (child.before)
        if i == 0:
            child.sendline(password)
            power_cycle_cmd = 'power outlets 1 cycle'
            child.sendline(power_cycle_cmd)
            # i = child.expect(['outlet', pexpect.TIMEOUT, pexpect.EOF], timeout=30)
            child.expect('y/n')
            child.sendline('y')
            child.expect(prompt_list)
            print (child.before)
