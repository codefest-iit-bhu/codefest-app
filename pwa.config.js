const { join } = require("path");

exports.webpack = function(config, env) {
  const src = config.context;
  config.resolve.alias["@styles"] = join(src, "styles");
  config.resolve.alias["@js"] = join(src, "js");
};
