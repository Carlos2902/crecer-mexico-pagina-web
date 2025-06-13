const shareConfig = document.getElementById("share-config");

const shareTextFacebook = shareConfig.dataset.facebook;
const shareTextTwitter = shareConfig.dataset.twitter;
const shareTextWhatsApp = shareConfig.dataset.whatsapp;

function shareOnFacebook() {
  const url = encodeURIComponent(window.location.origin);
  const text = encodeURIComponent(shareTextFacebook);
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}&quote=${text}`, '_blank');
}

function shareOnTwitter() {
  const url = encodeURIComponent(window.location.origin);
  const text = encodeURIComponent(shareTextTwitter);
  window.open(`https://twitter.com/intent/tweet?url=${url}&text=${text}`, '_blank');
}

function shareOnWhatsApp() {
  const url = encodeURIComponent(window.location.origin);
  const text = encodeURIComponent(`${shareTextWhatsApp} ${url}`);
  window.open(`https://wa.me/?text=${text}`, '_blank');
}