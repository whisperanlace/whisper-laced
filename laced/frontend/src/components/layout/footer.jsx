import React from "react";

const Footer = () => {
  return (
    <footer className="h-12 bg-ivory flex items-center justify-center shadow-inner">
      <p className="text-xs text-gray-500">
        &copy; {new Date().getFullYear()} Laced AI. All rights reserved.
      </p>
    </footer>
  );
};

export default Footer;
