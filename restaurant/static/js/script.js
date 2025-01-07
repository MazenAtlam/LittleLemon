$(document).ready(() => {
  const navbarNav = $(".navbar-nav")[0];
  const { pathname } = window.location;

  for (let i = 0; i < navbarNav.children.length; i++) {
    const navItem = navbarNav.children[i];
    const navLink = navItem.children[0];
    const navLinkHref = navLink.attributes.href.value;

    if (navLinkHref === pathname) {
      navLink.classList.add("disabled");
    } else {
      navLink.classList.remove("disabled");
    }
  }
});
