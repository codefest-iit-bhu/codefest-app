export const navigation = {
  hierarchy: {
    "~": {
      "": "/",
      events: {
        "": "/events",
        hackathon: "/events/1"
      },
      sponsors: {
        "": "/sponsors"
      },
      gallery: {
        "": "/gallery"
      },
      dashboard: {
        "": "/dashboard"
      }
    }
  },
  getPwdFromCurrent: function(current) {
    return current.split("/");
  },
  listContents: function(pwd) {
    var current = null;
    pwd.forEach(dir => {
      if (current) current = current[dir];
      else current = this.hierarchy[dir];
    });
    return current;
  }
};

export const terminal = {
  history: [
    {
      pwd: ["~"],
      status: 127,
      input: "as",
      output: "Invalid command."
    }
  ],
  getHistory: function() {
    return this.history;
  },
  addToHistory: function(pwd, status, input, output) {
    this.history.push({ pwd, status, input, output });
  }
};
