const { InjectManifest } = require("workbox-webpack-plugin");
const stylusLoader = require("stylus-loader");
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
  config.module.rules.forEach(({ test, use }) => {
    if ((test.test(".styl") || test.test(".stylus")) && Array.isArray(use)) {
      use.forEach((loader) => {
        if (loader.loader === "stylus-loader") {
          loader.options.import = [
            join(src, "styles/theme/index.styl"),
            join(src, "styles/mixins.styl"),
          ];
        } else loader;
      });
    }
  });
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
