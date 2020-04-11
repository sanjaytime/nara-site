// getQuote();

function getQuote() {
    fetch('https://api.kanye.rest')
        .then((resp) => resp.json())
        .then(function (data) {
            document.getElementById("quote").innerHTML = data.quote;

            const tweet = encodeURIComponent(`"${data.quote}"-@kanyewest via https://kanye.rest @ajzbc`);
            document.getElementById('tweet').href = `https://twitter.com/intent/tweet?text=${tweet}`;
        });
}

// copyEmail();

document.getElementById('emailButton').addEventListener('click', function(){
  var textarea = document.createElement('textarea');
  textarea.textContent = "sanjay@sanjaynara.com";
  document.body.appendChild(textarea);

  var selection = document.getSelection();
  var range = document.createRange();
//  range.selectNodeContents(textarea);
  range.selectNode(textarea);
  selection.removeAllRanges();
  selection.addRange(range);

  console.log('copy success', document.execCommand('copy'));
  selection.removeAllRanges();

  document.body.removeChild(textarea);
  alert("Copied my email address! (sanjay@sanjaynara.com)");

})
