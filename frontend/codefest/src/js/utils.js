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
