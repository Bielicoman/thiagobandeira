const fs = require('fs');

const videoIds = [
    'D43qNYNIIOA', 'efa_PSKMHLk', 'yrkck9BhKqo', 'rQlMRuub6vo', 
    'WeBx8Ewkm4I', 'yh_ZZTQN3-I', 'S3Uon0v7vS8', 'p6SIYQ2c2Bw', 
    'NwesZCYbSx0', 'b1ufVsXLPt8', 'vP7nbYS_DgY', 'KnDrc_qMJow'
];

async function getDates() {
    console.log("Fetching dates...");
    const results = [];
    for (const id of videoIds) {
        try {
            const res = await fetch(`https://www.youtube.com/watch?v=${id}`);
            const text = await res.text();
            const match = text.match(/"publishDate":"(.*?)"/);
            const date = match ? match[1] : '1970-01-01';
            results.push({ id, date });
            console.log(id, date);
        } catch (e) {
            console.log(id, 'Error');
        }
    }
    
    results.sort((a, b) => new Date(b.date) - new Date(a.date));
    console.log("\nSorted from newest to oldest:");
    results.forEach(r => console.log(r.id, r.date));
}

getDates();
