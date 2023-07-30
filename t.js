fetch
  .post("/consulta", { email: "m@m.com" })
  .success((res) => {
    console.log(res.data.msg);
  })
  .error((e) => {
    console.log(e.response.data.erro);
  });

try {
  let res = await fetch.post("/consulta", { email: "m@m.com" });

  console.log(res.data.msg);
} catch (e) {
  console.log(e.response.data.erro);
}
