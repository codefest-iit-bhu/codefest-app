export const navigation = {
  hierarchy: {
    "~": {
      "/": "/",
      events: {
        "/": "/events",
        hackathon: "/events/1"
      },
      sponsors: {
        "/": "/sponsors"
      },
      gallery: {
        "/": "/gallery"
      },
      dashboard: {
        "/": "/dashboard"
      }
    }
  },
  getPwdFromCurrent: function(current) {
    let rawPath = current.split("/");
    return rawPath.filter(el => !!el);
  },
  listContents: function(pwd) {
    var current = null;
    pwd.forEach(dir => {
      if (current) current = current[dir];
      else current = this.hierarchy[dir];
    });
    return current;
  },
  getTargetPageUrl: function(pwd, targetDir) {
    let hierarchy = this.listContents(pwd);
    let route = targetDir.split("/");
    let currentDir = null;
    route.forEach(dir => {
      if (currentDir) currentDir = currentDir[dir];
      else currentDir = hierarchy[dir];
    });
    return currentDir["/"];
  }
};

export const terminal = {
  history: [
    {
      // pwd: ["~"],
      // status: 127,
      // input: "as",
      // output: "Invalid command."
    }
  ],
  getHistory: function() {
    return this.history;
  },
  addToHistory: function(pwd, status, input, output) {
    this.history.push({ pwd, status, input, output });
  }
};
