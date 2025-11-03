module.exports = async function (context) {
  return {
    body: JSON.stringify({ message: "Hello from Node.js on OCI!" })
  };
};
