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
  <iframe
    style="width:100%; height:100%; position:fixed; top:0; bottom:0; left:0; right:0;"
    src="https://www.youtube-nocookie.com/embed/wew9zHCJYyI?autoplay=1&controls=0"
    frameborder="0"
    allowfullscreen>
  </iframe>
  <style>html {padding: 0; margin: 0}</style>
    `;
}

window.addEventListener("DOMContentLoaded", function () {
  konamiCode(showClip);
});
