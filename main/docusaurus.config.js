const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");
const math = require("remark-math");
const katex = require("rehype-katex");

/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: "JKUAT SES Data Structures and Algorithms",
  tagline: "JKUAT SES PROJECTS we build cool stuff",
  url: "https://jkuatses.github.io", //https://ses.jkuat.ac.ke/dsa
  baseUrl: "/dataStructuresAlgorithms/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon_io/favicon.ico",
  organizationName: "JKUATSES", // Usually your GitHub org/user name.
  projectName: "dataStructuresAlgorithms", // Usually your repo name.
  trailingSlash: false,
  themeConfig: {
    navbar: {
      title: "JKUAT SES Data Structures and Algorithms",
      logo: {
        alt: "JKUAT SES Data Structures and Algorithms Logo",
        src: "img/favicon_io/sesicon.svg",
      },
      items: [
        {
          type: "doc",
          docId: "intro",
          position: "left",
          label: "Tutorial",
        },
        { to: "/blog", label: "Blog", position: "left" },
        {
          href: "https://github.com/JKUATSES/dataStructuresAlgorithms",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Tutorial",
              to: "/docs/intro",
            },
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/JKUATSES",
            },
            {
              label: "LinkedIn",
              href:
                "https://ke.linkedin.com/company/jkuat-society-of-engineering-students",
            },
            {
              label: "Twitter",
              href: "https://twitter.com/jkuat_ses",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "Blog",
              to: "/blog",
            },
            {
              label: "GitHub",
              href: "https://github.com/JKUATSES",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: lightCodeTheme,
      darkTheme: darkCodeTheme,
    },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          remarkPlugins: [math],
          rehypePlugins: [katex],
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          editUrl:
            "https://github.com/JKUATSES/dataStructuresAlgorithms",
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          editUrl:
            "https://github.com/JKUATSES/dataStructuresAlgorithms",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
  stylesheets: [
    {
      href: "https://cdn.jsdelivr.net/npm/katex@0.13.11/dist/katex.min.css",
      integrity:
        "sha384-Um5gpz1odJg5Z4HAmzPtgZKdTBHZdw8S29IecapCSB31ligYPhHQZMIlWLYQGVoc",
      crossorigin: "anonymous",
    },
  ],
};
