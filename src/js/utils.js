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

export const isMinimal = function(mq) {
  return mq === "xs" || mq === "sm";
};

export const getRandom = function(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};

export const formatDateTo12HoursTime = function(date) {
  if (!(date instanceof Date))
    throw Error(`Date value expected, got ${date.constructor.name}`);
  return date.toLocaleString("en-us", {
    hour: "numeric",
    minute: "numeric",
    hour12: true
  });
};

/**
 * This function allow you to modify a JS Promise by adding some status properties.
 * Based on: http://stackoverflow.com/questions/21485545/is-there-a-way-to-tell-if-an-es6-promise-is-fulfilled-rejected-resolved
 * But modified according to the specs of promises : https://promisesaplus.com/
 */
export function MakeQuerablePromise(promise) {
  // Don't modify any promise that has been already modified.
  if (promise.isResolved) return promise;

  // Set initial state
  var isPending = true;
  var isRejected = false;
  var isFulfilled = false;

  // Observe the promise, saving the fulfillment in a closure scope.
  const result = promise.then(
    function(v) {
      isFulfilled = true;
      isPending = false;
      return v;
    },
    function(e) {
      isRejected = true;
      isPending = false;
      throw e;
    }
  );

  result.isFulfilled = function() {
    return isFulfilled;
  };
  result.isPending = function() {
    return isPending;
  };
  result.isRejected = function() {
    return isRejected;
  };
  return result;
}

export class TypingAnim {
  constructor(elem, msg) {
    this.elem = elem;
    this.msg = msg;
    this.shouldType = null;
  }

  _type() {
    if (!this.shouldType) return;
    this.elem.innerText = this.msg.substr(0, this._msgLength++);
    if (this._msgLength < this.msg.length + 1)
      requestAnimationFrame(this._type.bind(this));
  }

  _erase() {
    if (this.shouldType) return;
    this.elem.innerText = this.msg.substr(0, this._msgLength--);
    if (this._msgLength >= 0) requestAnimationFrame(this._erase.bind(this));
  }

  type() {
    this._msgLength = 0;
    this.shouldType = true;
    return this._type();
  }

  erase() {
    this._msgLength = this.elem.innerText.length;
    this.shouldType = false;
    return this._erase();
  }
}

export const interpolateEaseOutQuad = function(
  currentTime,
  startValue,
  endValue,
  animationDuration
) {
  endValue = endValue - startValue;
  currentTime /= animationDuration;
  return -endValue * currentTime * (currentTime - 2) + startValue;
};
