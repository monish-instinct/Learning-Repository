// popup.js

document.getElementById('reloadButton').addEventListener('click', function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      var activeTab = tabs[0];
      chrome.tabs.sendMessage(activeTab.id, { action: 'reload' });
    });
  });
  
  // Add a timer to automatically reload after 10 seconds of inactivity
  var inactivityTimer;
  
  function resetTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.sendMessage(activeTab.id, { action: 'reload' });
      });
    }, 10000); // 10 seconds
  }
  
  document.addEventListener('DOMContentLoaded', function () {
    resetTimer();
  });
  
  document.addEventListener('click', function () {
    resetTimer();
  });
  