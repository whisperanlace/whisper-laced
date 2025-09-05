import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Sidebar from "./components/layout/Sidebar";
import Topbar from "./components/layout/Topbar";

import Home from "./routes/Home";
import Generate from "./routes/Generate";
import Models from "./routes/Models";
import History from "./routes/History";
import Settings from "./routes/Settings";

import { AppContextProvider } from "./context/AppContext";
import { WhisperContextProvider } from "./context/WhisperContext";

function App() {
  return (
    <AppContextProvider>
      <WhisperContextProvider>
        <Router>
          <div className="flex h-screen bg-ivory">
            <Sidebar />
            <div className="flex-1 flex flex-col">
              <Topbar />
              <main className="flex-1 overflow-auto p-4">
                <Routes>
                  <Route path="/" element={<Home />} />
                  <Route path="/generate" element={<Generate />} />
                  <Route path="/models" element={<Models />} />
                  <Route path="/history" element={<History />} />
                  <Route path="/settings" element={<Settings />} />
                </Routes>
              </main>
            </div>
          </div>
        </Router>
      </WhisperContextProvider>
    </AppContextProvider>
  );
}

export default App;
