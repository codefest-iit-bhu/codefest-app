export const isMobile = function() {
  if (
    /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
      navigator.userAgent
    )
  ) {
    return true;
  } else {
    return false;
  }
};

export const getRandom = function(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};

export const animateTyping = function(elem, msg) {
  var msgLength = 0;
  function type() {
    elem.innerHTML = msg.substr(0, msgLength++);
    if (msgLength < msg.length + 1) requestAnimationFrame(type);
  }
  return type();
};

export const animateErasing = function(elem, msg) {
  var msgLength = msg.length;
  function erase() {
    elem.innerHTML = msg.substr(0, msgLength--);
    if (msgLength >= 0) requestAnimationFrame(erase);
  }
  return erase();
};
