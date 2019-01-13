import Vue from 'vue';
import GAnalytics from 'ganalytics';
import App from '@components/App';
import router from './router';
import './index.styl';

Vue.config.productionTip = false;
const render = h => h(App);

// Mount w/ Hydration
// ~> because HTML already exists from`pwa export`
// @see https://ssr.vuejs.org/guide/hydration.html
new Vue({ router, render }).$mount('#app', true);

if (process.env.NODE_ENV === 'production') {
	window.ga = new GAnalytics('UA-XXXXXXXX-X');

	router.afterEach(nxt => {
		ga.send('pageview', { dp: nxt.path });
	});

	// Service Worker registration
	if ('serviceWorker' in navigator) {
		navigator.serviceWorker.register('/sw.js');
	}
}
