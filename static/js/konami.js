function konamiCode(callback) {
  // The famous Konami sequence in keycodes
  // up up down down left right left right b a
  var sequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
  var ko = Array.from(sequence);

  // Get the rest of this function's arguments (if any).
  // These will be used as the callback's arguments.
  var args = [];
  for (var i = 1; i < arguments.length; i++) {
    args.push(arguments[i]);
  }

  document.addEventListener("keydown", function (e) {
    if (e.keyCode === ko[0]) {
      ko.splice(0, 1);
      if (ko.length === 0) {
        callback.apply(null, args);
      }
    } else {
      ko = Array.from(sequence);
    }
  });
}

function showClip() {
  document.body.innerHTML = `
  <video autoplay controls style="height:99vh; width:100%;">
    <source src="https://junk.imnhan.com/hsg-op.mp4" type="video/mp4">
  </video>
  <style>html {padding: 0; margin: 0}</style>
    `;
}

window.addEventListener("DOMContentLoaded", function () {
  konamiCode(showClip);
});
