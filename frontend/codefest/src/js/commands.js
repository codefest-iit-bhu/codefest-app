import { navigation } from "./store";
import "./exceptions";
import { CommandInvalidEnvironment } from "./exceptions";

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
        resolve(that.run().html());
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

class ColumnOutput extends BaseOutput {
  processData(envs) {
    let vue = envs.vue;
    let result = "";
    this.data.forEach(elem => (result += `${elem} `));
    this._html = `<div class="${vue.$style.column}">${result}</div>`;
  }
}

export class ListDirCommand extends BaseCommand {
  static getCommandName() {
    return "ls";
  }

  run() {
    let pwd = this.envs.pwd;
    if (!pwd) throw new CommandInvalidEnvironment();
    let list = navigation.listContents(pwd);
    let result = [];
    for (let key in list) {
      let name = key;
      let url = list[key]["/"] || list["/"];
      result.push(`<router-link to="${url}">${name}</router-link>`);
    }
    return new ColumnOutput(result, this.envs);
  }
}

export class ChangeDirCommand extends BaseCommand {
  static getCommandName() {
    return "cd";
  }
}

export const CommandList = [ListDirCommand, ChangeDirCommand];
