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

// Source: https://hackernoon.com/copying-text-to-clipboard-with-javascript-df4d4988697f
export const copyToClipboard = str => {
  const el = document.createElement("textarea"); // Create a <textarea> element
  el.value = str; // Set its value to the string that you want copied
  el.setAttribute("readonly", ""); // Make it readonly to be tamper-proof
  el.style.position = "absolute";
  el.style.left = "-9999px"; // Move outside the screen to make it invisible
  document.body.appendChild(el); // Append the <textarea> element to the HTML document
  const selected =
    document.getSelection().rangeCount > 0 // Check if there is any content selected previously
      ? document.getSelection().getRangeAt(0) // Store selection if found
      : false; // Mark as false to know no selection existed before
  el.select(); // Select the <textarea> content
  document.execCommand("copy"); // Copy - only works as a result of a user action (e.g. click events)
  document.body.removeChild(el); // Remove the <textarea> element
  if (selected) {
    // If a selection existed before copying
    document.getSelection().removeAllRanges(); // Unselect everything on the HTML document
    document.getSelection().addRange(selected); // Restore the original selection
  }
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

if (typeof String.prototype.trim === "undefined") {
  String.prototype.trim = function() {
    return String(this).replace(/^\s+|\s+$/g, "");
  };
}
