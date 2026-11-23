const scriptPicker = document.querySelector('#sample-script');
const sampleVariants = document.querySelectorAll('.sample-notation [data-script]');

function showSelectedScript() {
  const selectedScript = scriptPicker.querySelector('input:checked').value;
  for (const variant of sampleVariants) {
    variant.hidden = variant.dataset.script !== selectedScript;
  }
}

scriptPicker.addEventListener('change', showSelectedScript);
window.addEventListener('pageshow', showSelectedScript);
showSelectedScript();
scriptPicker.hidden = false;
