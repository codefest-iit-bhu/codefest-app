export class CommandBaseError extends Error {
  constructor(...args) {
    super(...args);
    Error.captureStackTrace(this, CommandBaseError);
    this.code = -1;
  }
}

export class CommandNotFoundError extends CommandBaseError {
  constructor(...args) {
    super(...args);
    this.message = "Command not found.";
    this.code = 127;
  }
}
