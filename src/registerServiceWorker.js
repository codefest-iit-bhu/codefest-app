let wb;

if ("serviceWorker" in navigator) {
  const initWorkbox = async () => {
    const { Workbox } = await import("workbox-window");
    wb = new Workbox(`/sw.js`);

    wb.addEventListener("controlling", () => {
      window.location.reload();
    });

    wb.register();
  };
  initWorkbox();
} else {
  wb = null;
}

export default wb;
