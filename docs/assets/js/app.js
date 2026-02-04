const tabs = document.querySelectorAll(".tab");
const panels = document.querySelectorAll(".tab-panel");

tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((item) => item.classList.remove("tab--active"));
    panels.forEach((panel) => panel.classList.remove("tab-panel--active"));

    tab.classList.add("tab--active");
    const targetPanel = document.getElementById(tab.dataset.tab);
    if (targetPanel) {
      targetPanel.classList.add("tab-panel--active");
    }
  });
});
