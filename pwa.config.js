const { InjectManifest } = require("workbox-webpack-plugin");
const { join } = require("path");

exports.webpack = function(config, env) {
  // Add module aliases
  const src = config.context;
  config.resolve.alias["@styles"] = join(src, "styles");
  config.resolve.alias["@js"] = join(src, "js");
  config.resolve.alias["@store"] = join(src, "store");
  config.devServer.host = "0.0.0.0";

  // Add Workbox plugin
  config.plugins.push(
    new InjectManifest({
      swSrc: join(src, "sw.js"),
    })
  );
};

exports.brotli = {
  cache: true,
  threshold: 0,
  minRatio: 0.8,
  compressionOptions: {
    quality: 11,
    size_hint: 0,
    lgblock: 0,
    lgwin: 22,
    mode: 0,
  },
};
