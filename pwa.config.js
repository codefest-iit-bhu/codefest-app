const { join } = require("path");

exports.webpack = function(config, env) {
  const src = config.context;
  config.resolve.alias["@styles"] = join(src, "styles");
  // config.stylus = {
  //   preferPathResolver: "webpack"
  // };
};
