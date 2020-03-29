import Vue from 'vue'
import anchorme from 'anchorme'

const FilterPlugin = {
  install(Vue) {
    Vue.filter('anchor', (value) => {
      return anchorme(value)
    })
  },
  version: '1.0.0'
}

Vue.use(FilterPlugin)
