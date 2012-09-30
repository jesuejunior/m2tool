from modargs import args
import sys
import m2tool.commands


def main():
    command, params = args.parse(sys.argv[1:])
    all_commands = args.available_commands(m2tool.commands)

    print params
    if command not in all_commands:
        print "Command {0} not found!".format(command)

    else:
        print "Running {0}".format(command)
        f = args.function_for(m2tool.commands, command)
        f(**params)

    sys.exit(0)
