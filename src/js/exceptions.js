export class CommandBaseError extends Error {
  constructor(...args) {
    super(...args);
    Error.captureStackTrace(this, CommandBaseError);
    this.code = -1;
  }
}

export class CommandInvalidInput extends CommandBaseError {
  constructor(code, msg, ...args) {
    super(...args);
    this.code = code;
    this.message = msg;
  }
}

export class CommandInvalidEnvironment extends CommandBaseError {
  constructor(...args) {
    super(...args);
    this.code = 111;
    this.message = "Weirdly, the command is run in a wrong environment.";
  }
}

export class CommandNotFoundError extends CommandBaseError {
  constructor(...args) {
    super(...args);
    this.message = "Command not found.";
    this.code = 127;
  }
}
