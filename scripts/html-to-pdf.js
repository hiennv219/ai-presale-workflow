#!/usr/bin/env node
const puppeteer = require("puppeteer");
const path = require("path");

const [, , htmlPath, pdfPath] = process.argv;

if (!htmlPath || !pdfPath) {
  console.error("Usage: html-to-pdf.js <input.html> <output.pdf>");
  process.exit(1);
}

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();

  const fileUrl = "file://" + path.resolve(htmlPath);
  await page.goto(fileUrl, { waitUntil: "networkidle0" });

  const isLandscape = await page.evaluate(() =>
    document.body.classList.contains("has-landscape")
  );

  await page.pdf({
    path: path.resolve(pdfPath),
    format: "A4",
    landscape: isLandscape,
    printBackground: true,
    margin: { top: "15mm", bottom: "15mm", left: "12mm", right: "12mm" },
  });

  await browser.close();
  console.log(`✔ PDF exported: ${pdfPath}`);
})();
