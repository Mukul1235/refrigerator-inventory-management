import React, { useEffect, useState } from "react";
import { fetchExpiryAlerts } from "../Api/Api";
import "../styles/ExpiryAlerts.css"; 

function ExpiryAlerts() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      const response = await fetchExpiryAlerts();
      setAlerts(response.data);
    };
    fetchAlerts();
  }, []);

  return (
    <div className="expiry-alerts-container">
      <h2>Expiry Alerts</h2>
      {alerts.length > 0 ? (
        alerts.map((alert) => (
          <p key={alert.id} className="expiry-alert">
            {alert.name} is expiring soon!
          </p>
        ))
      ) : (
        <p className="no-alerts">No alerts</p>
      )}
    </div>
  );
}

export default ExpiryAlerts;