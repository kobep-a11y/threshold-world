export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const secret = req.headers['x-threshold-secret'];
  if (secret !== process.env.THRESHOLD_SECRET) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  const { content } = req.body;
  if (!content) {
    return res.status(400).json({ error: 'Missing content' });
  }

  try {
    const encodedContent = Buffer.from(content).toString('base64');

    const response = await fetch(
      `https://api.github.com/repos/${process.env.GITHUB_REPO}/dispatches`,
      {
        method: 'POST',
        headers: {
          'Authorization': `token ${process.env.GITHUB_TOKEN}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          event_type: 'update-site',
          client_payload: { content: encodedContent }
        })
      }
    );

    if (!response.ok) throw new Error('GitHub API error');
    return res.status(200).json({ success: true });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}
