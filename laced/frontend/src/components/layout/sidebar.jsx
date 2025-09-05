import React from "react";
import { NavLink } from "react-router-dom";
import icons from "../assets/icons"; // optional central import if needed

const Sidebar = () => {
  const links = [
    { name: "Home", path: "/", icon: "/assets/icons/home.svg" },
    { name: "Generate", path: "/generate", icon: "/assets/icons/generate.svg" },
    { name: "Models", path: "/models", icon: "/assets/icons/models.svg" },
    { name: "History", path: "/history", icon: "/assets/icons/history.svg" },
    { name: "Settings", path: "/settings", icon: "/assets/icons/settings.svg" },
  ];

  return (
    <aside className="w-20 bg-wine-red flex flex-col items-center py-4 space-y-4">
      {links.map(link => (
        <NavLink
          key={link.name}
          to={link.path}
          className={({ isActive }) =>
            `flex flex-col items-center justify-center p-2 rounded hover:bg-gold transition ${
              isActive ? "bg-gold" : "bg-transparent"
            }`
          }
        >
          <img src={link.icon} alt={link.name} className="w-6 h-6 mb-1" />
          <span className="text-xs text-ivory">{link.name}</span>
        </NavLink>
      ))}
    </aside>
  );
};

export default Sidebar;
