import { join } from 'path'

export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [
      {
        rel: 'stylesheet',
        href: 'https://use.fontawesome.com/releases/v5.7.2/css/all.css',
        integrity:
          'sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr',
        crossorigin: 'anonymous'
      },
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
    script: [
      {
        src: 'https://cdnjs.cloudflare.com/ajax/libs/gsap/2.1.2/TweenMax.min.js'
      },
      {
        src:
          'https://cdnjs.cloudflare.com/ajax/libs/gsap/2.1.2/plugins/ScrollToPlugin.min.js'
      }
    ]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  srcDir: 'src',
  /*
   ** Global CSS
   */
  css: ['~/assets/styles/index.styl'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    {
      src: '~/plugins/vue2-scrollspy',
      ssr: false
    },
    {
      src: '~/plugins/vue-youtube'
    },
    {
      src: '~/plugins/filters'
    }
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    [
      '@nuxt/typescript-build',
      {
        typeCheck: false
      }
    ]
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    [
      'nuxt-mq',
      {
        breakpoints: {
          __: 320,
          xs: 575,
          sm: 767,
          md: 991,
          lg: 1367,
          xl: 1920,
          xxl: Infinity
        },
        defaultBreakpoint: 'lg'
      }
    ],
    ['@nuxtjs/device']
  ],
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, _ctx) {
      const srcDir = join(__dirname, 'src')
      const assetDir = join(srcDir, 'assets')
      // config.resolve.alias = {
      //   '~': srcDir,
      //   '@js': join(assetDir, 'js'),
      //   '@styles': join(assetDir, 'styles'),
      //   '@components': join(srcDir, 'components')
      // }
      delete config.resolve.alias['@']
      config.resolve.alias.vue = 'vue/dist/vue.common'
      config.resolve.alias['@styles'] = join(assetDir, 'styles')
      config.resolve.alias['@js'] = join(assetDir, 'js')
      config.resolve.alias['@components'] = join(srcDir, 'components')
    },
    loaders: {
      stylus: {
        preferPathResolver: 'webpack',
        import: [
          join(__dirname, 'src/assets/styles/theme/index.styl'),
          join(__dirname, 'src/assets/styles/mixins.styl')
        ]
      }
    }
  }
}
