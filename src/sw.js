importScripts("./workbox-v4.3.1.js");

if (workbox) {
  workbox.precaching.precacheAndRoute(self.__WB_MANIFEST);
} else {
  console.warn("Boo! Workbox did not load!");
}
