<script lang="ts">
  import { onMount } from 'svelte';

  let videoId: string = "";


  async function handleSubmit(event: Event) {

    console.log(videoId);

    try {
      const response = await fetch('http://localhost:5000/api/download', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          url: videoId,
        })
      });

      const data = await response.json();
      window.open(data.url, '_blank');

    } catch (error) {

      console.error(error);

    }
  }

</script>

<div class="h-screen flex justify-center items-center">
  <div class="bg-white dark:bg-slate-800 rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl w-2/4 m-6">
    <h3 class="text-slate-900 dark:text-white text-lg font-medium mb-6">YouTube Video Downloader</h3>

    <form on:submit={handleSubmit}>
      <div class="mb-4">
        <label for="videoLink" class="block text-slate-900 dark:text-white mb-2">Video Link</label>
        <input type="text" id="videoLink" name="videoLink" bind:value={videoId} class="w-full px-3 py-2 border border-slate-300 rounded-md focus:outline-none focus:ring focus:ring-slate-200" placeholder="Enter YouTube video link" required>
      </div>


      <button type="submit" class="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-medium py-2 rounded-md">
        Submit
      </button>
    </form>
  </div>
</div>
