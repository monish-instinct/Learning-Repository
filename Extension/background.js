chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.action === 'reload') {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var activeTab = tabs[0];
        chrome.tabs.reload(activeTab.id);
      });
    }
  });
  