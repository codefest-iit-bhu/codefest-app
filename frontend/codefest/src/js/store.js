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
