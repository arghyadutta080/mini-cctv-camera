
const VideoFeed = () => {
    return (
        <div>
            <h2>Live CCTV Feed</h2>
            <img
                src="http://127.0.0.1:5000/video_feed"
                alt="CCTV Feed"
                style={{ width: '100%', height: 'auto' }}
            />
        </div>
    );
};

export default VideoFeed;
