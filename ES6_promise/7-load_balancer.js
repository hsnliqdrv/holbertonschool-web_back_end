export default async function loadBalancer(chinaDownload, USDownload) {
  const fastest = await Promise.race([chinaDownload, USDownload]);
  return fastest; 
}