def ignore_command(command):
    ignore = ["alias", "configuration", "ip", "sql", "select", "update", "exec", "del", "truncate"]
    return command in ignore
    
print(ignore_command("dв"))

 

