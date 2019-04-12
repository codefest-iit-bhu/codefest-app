const { join } = require("path");

exports.webpack = function(config, env) {
  const src = config.context;
  config.resolve.alias["@styles"] = join(src, "styles");
  config.resolve.alias["@js"] = join(src, "js");
  config.resolve.alias["@store"] = join(src, "store");
  config.devServer.host = "0.0.0.0";
};
