// Progressive enhancement: without JavaScript, all research tracks remain readable.
const tabList = document.querySelector('.research-tabs');
const tabs = [...tabList.querySelectorAll('button[data-track]')];
const panels = [...document.querySelectorAll('[data-panel]')];

function selectTrack(selected, focus = false) {
  for (const tab of tabs) {
    const active = tab === selected;
    tab.setAttribute('aria-selected', String(active));
    tab.tabIndex = active ? 0 : -1;
  }
  for (const panel of panels) panel.hidden = panel.dataset.panel !== selected.dataset.track;
  if (focus) selected.focus();
}

tabList.setAttribute('role', 'tablist');
for (const panel of panels) {
  panel.setAttribute('role', 'tabpanel');
  panel.tabIndex = 0;
}
for (const tab of tabs) {
  tab.setAttribute('role', 'tab');
  tab.addEventListener('click', () => selectTrack(tab));
  tab.addEventListener('keydown', (event) => {
    const index = tabs.indexOf(tab);
    let next;
    if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
    if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
    if (event.key === 'Home') next = 0;
    if (event.key === 'End') next = tabs.length - 1;
    if (next === undefined) return;
    event.preventDefault();
    selectTrack(tabs[next], true);
  });
}
selectTrack(tabs[0]);
document.querySelector('#year').textContent = new Date().getFullYear();
