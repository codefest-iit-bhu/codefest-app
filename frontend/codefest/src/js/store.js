export const navigation = {
  hierarchy: {
    "~": {
      "/": "/",
      events: {
        "/": "/events",
        hackathon: "/events/1"
      }
    }
  },
  getPwdFromCurrent: function(current) {
    if (!current) return [];
    let rawPath = current.split("/");
    return rawPath.filter(el => !!el);
  },
  getLinksFromPwd: function(pwd) {
    var current = null;
    var result = [];
    pwd.forEach(dir => {
      if (current) current = current[dir];
      else current = this.hierarchy[dir];
      result.push(current["/"]);
    });
    return result;
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
    let backNav = targetDir.match(/^(..\/)(..\/)*?/g);

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
  history: [],
  getHistory: function() {
    return this.history;
  },
  addToHistory: function(pwd, status, input, output) {
    this.history.push({ pwd, status, input, output });
  }
};
