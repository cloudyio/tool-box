<script lang="ts">
    async function handleSubmit(event: Event) {
      event.preventDefault();
      
      const videoLink = (event.target as HTMLFormElement).videoLink.value;
      const resolution = (event.target as HTMLFormElement).resolution.value;
      
      try {
        const response = await fetch('http://localhost:5000/download', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            video_link: videoLink,
            resolution: resolution
          })
        });
        
        const data = await response.json();
        console.log(data);
        
        // Handle the response data as per your requirement
      } catch (error) {
        console.error(error);
        
        // Handle the error as per your requirement
      }
    }
  </script>
  
  <div class="h-screen flex justify-center items-center">
    <div class="bg-white dark:bg-slate-800 rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl w-2/4 m-6">
      <h3 class="text-slate-900 dark:text-white text-lg font-medium mb-6">YouTube Video Downloader</h3>
  
      <form on:submit="{handleSubmit}">
        <div class="mb-4">
          <label for="videoLink" class="block text-slate-900 dark:text-white mb-2">Video Link</label>
          <input type="text" id="videoLink" name="videoLink" class="w-full px-3 py-2 border border-slate-300 rounded-md focus:outline-none focus:ring focus:ring-slate-200" placeholder="Enter YouTube video link" required>
        </div>
  
        <div class="mb-4">
          <label for="resolution" class="block text-slate-900 dark:text-white mb-2">Resolution</label>
          <div class="flex space-x-2">
            <button type="button" name="resolution" value="720p" class="w-20 h-10 text-center bg-gray-300 hover:bg-gray-400 focus:bg-indigo-600 rounded-md transition-colors duration-200 focus:outline-none">720p</button>
            <button type="button" name="resolution" value="1080p" class="w-20 h-10 text-center bg-gray-300 hover:bg-gray-400 focus:bg-indigo-600 rounded-md transition-colors duration-200 focus:outline-none">1080p</button>
            <button type="button" name="resolution" value="1440p" class="w-20 h-10 text-center bg-gray-300 hover:bg-gray-400 focus:bg-indigo-600 rounded-md transition-colors duration-200 focus:outline-none">1440p</button>
          </div>
        </div>
  
        <button type="submit" class="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-medium py-2 rounded-md">
          Submit
        </button>
      </form>
    </div>
  </div>
  