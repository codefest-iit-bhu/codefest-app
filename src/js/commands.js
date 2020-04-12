import { navigation, terminal } from "@store/navigation";
import * as Exception from "./exceptions";

class BaseCommand extends Object {
  constructor(args, envs) {
    super(arguments);
    this.args = args;
    this.envs = envs;
  }

  execute() {
    var that = this;
    return new Promise(function(resolve, reject) {
      try {
        that.validateInput();
        let result = that.run();
        if (result) resolve(result.html());
        else resolve("");
      } catch (error) {
        reject(error);
      }
    });
  }

  validateInput() {}

  run() {}

  static getCommandName() {
    return null;
  }

  static isValid(cmd) {
    return !!this.getCommandName() && cmd === this.getCommandName();
  }
}

class BaseOutput extends Object {
  constructor(data, envs) {
    super(arguments);
    this.data = data;
    this.processData(envs);
  }

  processData(envs) {
    this._html = this.data;
  }

  html() {
    return this._html;
  }
}

class NullOutput extends Object {
  html() {
    return null
  }
}

class ColumnOutput extends BaseOutput {
  processData(envs) {
    let vue = envs.vue;
    let result = "";
    this.data.forEach((elem) => (result += `${elem} `));
    this._html = `<div class="${vue.$style.column}">${result}</div>`;
  }
}

class ListDirCommand extends BaseCommand {
  static getCommandName() {
    return "ls";
  }

  validateInput() {
    if (this.args.length > 1)
      throw new Exception.CommandInvalidInput(1, "Invalid arguments provided");
  }

  run() {
    let pwd = this.envs.pwd;
    if (!pwd) throw new Exception.CommandInvalidEnvironment();
    let list = navigation.listContents(pwd);

    let targetDir = this.args[0];
    if (targetDir) {
      if (!list[targetDir])
        throw new Exception.CommandInvalidInput(2, "Directory not found.");
      list = navigation.listContents(pwd.concat(targetDir));
    }

    let result = [];
    for (let key in list) {
      if (!list[key]) continue;
      result.push(`<router-link to="${list[key]}">${key}</router-link>`);
    }
    return new ColumnOutput(result, this.envs);
  }
}

class ChangeDirCommand extends BaseCommand {
  static getCommandName() {
    return "cd";
  }

  validateInput() {
    if (this.args.length > 1)
      throw new Exception.CommandInvalidInput(1, "Invalid arguments provided");
  }

  run() {
    let vue = this.envs.vue;
    let pwd = this.envs.pwd;
    let url;
    if (this.args.length === 0) {
      url = "/";
    } else {
      let targetDir = this.args[0].trim();
      try {
        url = navigation.getTargetPageUrl(pwd, targetDir);
      } catch (error) {
        throw new Exception.CommandInvalidInput(2, "Directory not found.");
      }
      if (!url)
        throw new Exception.CommandInvalidInput(2, "Directory not found.");
    }
    vue.$router.push(url);
  }
}

class ClearCommand extends BaseCommand {
  static getCommandName() {
    return "clear";
  }

  run() {
    terminal.clearHistory();
    return new NullOutput()
  }
}

class HelpCommand extends BaseCommand {
  static getCommandName() {
    return "help";
  }

  run() {
    return new BaseOutput(
      `Glad that you are one of the geeky nerds to visit this site and use this terminal!
    It is just a pretty basic shell and has only 5 simple commands - ls, cd, toggle, clear and help (the one with this output).`,
      this.envs
    );
  }
}

class ToggleThemeCommand extends BaseCommand {
  static getCommandName() {
    return "toggle";
  }

  run() {
    this.envs.vue.$store.dispatch("toggle_theme");
  }
}

export const CommandList = [
  ListDirCommand,
  ChangeDirCommand,
  ClearCommand,
  HelpCommand,
  ToggleThemeCommand,
];
