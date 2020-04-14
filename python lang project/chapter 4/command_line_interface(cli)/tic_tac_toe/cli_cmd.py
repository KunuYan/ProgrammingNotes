import ttc_logic, ttc_cli, cmd


class cli_cmd(cmd.Cmd):
    # commands name must mach a function with same name starting with do_
    intro = "Enter a command: new, restore, quit. Type 'help' or '?' for help"
    prompt = "(ttc) "
    game = ""

    def do_new(self, arg):  # the cmd.Cmd class interpret the part after '_' as command user can type.
        self.game = ttc_logic.newGame()
        ttc_cli.playGame(self.game)

    def do_restore(self, arg):
        self.game = ttc_logic.restoreGame()
        ttc_cli.playGame(self.game)

    def do_quit(self, arg):
        print("Goodbye...")
        raise SystemExit


def main():
    game = cli_cmd().cmdloop()


if __name__ == "__main__":
    main()
