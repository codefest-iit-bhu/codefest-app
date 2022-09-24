import anchorme from "anchorme";

export default {
  install(Vue) {
    Vue.filter("anchor", value => {
      return anchorme(value);
    });
  }
};
export const version = "1.0.0";
